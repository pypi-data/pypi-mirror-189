use pyo3::prelude::*;

#[pyclass]
#[derive(Debug)]
pub struct TickData {
    #[pyo3(get)]
    pub(crate) update_id: u64,
    #[pyo3(get)]
    pub(crate) symbol: String,
    #[pyo3(get)]
    pub(crate) bid: String,
    #[pyo3(get)]
    pub(crate) bid_size: String,
    #[pyo3(get)]
    pub(crate) ask: String,
    #[pyo3(get)]
    pub(crate) ask_size: String,  // ask_size
}

#[pymethods]
impl TickData {
    // For `__repr__` we want to return a string that Python code could use to recreate
    // the `Number`, like `Number(5)` for example.
    fn __repr__(&self) -> String {
        // We use the `format!` macro to create a string. Its first argument is a
        // format string, followed by any number of parameters which replace the
        // `{}`'s in the format string.
        format!("TickData: bid={bid} ask={ask}",
                ask = &self.ask,
                bid = &self.bid,
        )
    }

    // `__str__` is generally used to create an "informal" representation, so we
    // just forward to `i32`'s `ToString` trait implementation to print a bare number.
    fn __str__(&self) -> String {
        self.__repr__()
    }
}
