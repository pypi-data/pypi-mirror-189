use circuit_base::{
    expand_node::ExpandError,
    generalfunction::GeneralFunctionShapeError,
    module::SubstitutionError,
    named_axes::NamedAxesError,
    parsing::{ParseCircuitError, ReferenceCircError},
    ConstructError, TensorEvalError,
};
use circuit_rewrites::{
    algebraic_rewrite::{DistributeError, PushDownIndexError},
    batching::BatchError,
    deep_rewrite::SimpConfigError,
    scheduled_execution::{SchedulingError, SchedulingOOMError},
};
use get_update_node::{iterative_matcher::IterativeMatcherError, sampler::SampleError};
use nb_operations::{
    cumulant_rewrites::CumulantRewriteError,
    modules::{ExtractSymbolsError, ModuleBindError, PushDownModuleError},
    nest::NestError,
};
use pyo3::{
    exceptions::PyException, pyclass, pymethods, types::PyModule, Py, PyErr, PyObject, PyResult,
    Python,
};
use rr_util::{
    errors_util::HasPythonException,
    rearrange_spec::{PermError, RearrangeParseError, RearrangeSpecError},
    symbolic_size::{SymbolicSizeOverflowError, SymbolicSizeSetError},
    tensor_util::{IndexError, MiscInputError, ParseError},
};

// TODO: remove when/if we drop 3.11 support
#[pyclass(extends=PyException)]
pub struct ExceptionWithRustContext {
    #[pyo3(get)]
    exc: PyObject,
    #[pyo3(get)]
    context: Vec<String>,
}

#[pymethods]
impl ExceptionWithRustContext {
    fn __str__(&self) -> PyResult<String> {
        Python::with_gil(|py| {
            let x: &str = &self.exc.as_ref(py).str()?.to_string_lossy();
            Ok(if self.context.len() == 0 {
                x.to_owned()
            } else {
                format!("{}\n{}\n  (this is an ExceptionWithRustContext, access e.exc or upgrade to 3.11 to get the underlying exception)", x, self.context.join("\n"))
            })
        })
    }
}

macro_rules! setup_errors {
    ($($t:ty),* $(,)?) => {
        pub fn anyhow_to_py_err(err: anyhow::Error) -> PyErr {
            $(
                if let Some(x) = err.root_cause().downcast_ref::<$t>() {
                    return x.get_py_err(format!("{:?}", err));
                }
            )*

            pyo3::anyhow::anyhow_to_py_err(&err, |py, e, msgs|
                PyErr::from_value(Py::new(py, ExceptionWithRustContext { exc: e.into_value(py).into(), context: msgs }).unwrap().as_ref(py)) )
        }
        pub fn register_exceptions(py: Python<'_>, m: &PyModule) -> PyResult<()> {
            $(
                <$t>::register(py, m)?;
            )*
            Ok(())
        }
        pub fn print_exception_stubs(py : Python<'_>) -> PyResult<String> {
            let out = [
                $(
                    <$t>::print_stub(py)?,
                )*
            ].join("\n");
            Ok(out)
        }
    };
}

setup_errors!(
    BatchError,
    ConstructError,
    ExpandError,
    SubstitutionError,
    MiscInputError,
    ParseError,
    ParseCircuitError,
    RearrangeSpecError,
    PermError,
    RearrangeParseError,
    SchedulingError,
    SchedulingOOMError,
    TensorEvalError,
    SampleError,
    IndexError,
    NestError,
    PushDownIndexError,
    DistributeError,
    SimpConfigError,
    CumulantRewriteError,
    GeneralFunctionShapeError,
    ReferenceCircError,
    SymbolicSizeOverflowError,
    SymbolicSizeSetError,
    IterativeMatcherError,
    ModuleBindError,
    NamedAxesError,
    PushDownModuleError,
    ExtractSymbolsError
);
