use std::pin::Pin;
use crate::binance_connector::{BinanceListener, BinanceListenerOptions};

mod binance_connector;

const MEEP: &'static str = "meep";
static SECOND_MEEP: &'static str = "meep2";

fn f(x: &u8, y: &u8) -> &u8 {
    &10
}

fn main() {
    let a = f(&1,&2);
    dbg!(a);

    // let ticker_symbols = vec![
    //     "1inchusdt", "aaveusdt", "adausdt", "algousdt",
    //     "aliceusdt", "ankrusdt", "antusdt", "apeusdt", "atomusdt",
    //     "avaxusdt", "axsusdt", "balusdt"];
    // let tickers: Vec<String> = ticker_symbols.iter().map(|t| format!("{}@bookTicker", t)).collect();
    //
    // let it = BinanceListener::new(Some("ff".to_string()));
    //
    // let opts = BinanceListenerOptions::new(tickers);
    //
    // let callback = |t| { dbg!(&t); };
    //
    // it.subscribe(opts, &callback);
}