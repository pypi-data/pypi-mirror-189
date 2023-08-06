mod binance_connector;
mod python;

use std::rc::Rc;
use binance::model::BookTickerEvent;
use python::models::TickData;

use pyo3::prelude::*;
use crate::binance_connector::{BinanceListener, BinanceListenerOptions};

#[pyclass]
struct ExchangeListener {
    token: Option<String>,
}

#[pymethods]
impl ExchangeListener {
    #[new]
    fn new(token: Option<String>) -> ExchangeListener {
        ExchangeListener { token }
    }

    fn subscribe(&self, py: Python<'_>, tickers: Vec<String>, callback: PyObject) {
        // let ticker_symbols = vec![
        //     "1inchusdt", "aaveusdt", "adausdt", "algousdt",
        //     "aliceusdt", "ankrusdt", "antusdt", "apeusdt", "atomusdt",
        //     "avaxusdt", "axsusdt", "balusdt"];
        // let tickers: Vec<String> = ticker_symbols.iter().map(|t| format!("{}@bookTicker", t)).collect();

        let it: BinanceListener = BinanceListener::new(Some("ff".to_string()));
        let opts = BinanceListenerOptions::new(tickers);

        let handler = move |t: BookTickerEvent| {
            let guard = Python::acquire_gil();
            let py = guard.python();
            // let py = py.clone();
            // dbg!(py);

            let tick = TickData {
                update_id: t.update_id,
                symbol: t.symbol,
                bid: t.best_bid,
                bid_size: t.best_bid_qty,
                ask: t.best_ask,
                ask_size: t.best_ask_qty,
            };

            // dbg!(&t);
            // println!("11");
            callback.call(py, (tick, ), None).expect("TODO: panic message");
        };

        it.subscribe(opts, &handler);

        // callback.call(py, (tick, ), None).expect("TODO: panic message");
    }
}


/// A Python module implemented in Rust. The name of this function must match
/// the `lib.name` setting in the `Cargo.toml`, else Python will not be able to
/// import the module.
#[pymodule]
fn exchange_worker(_py: Python<'_>, m: &PyModule) -> PyResult<()> {
    m.add_class::<ExchangeListener>()?;
    Ok(())
}