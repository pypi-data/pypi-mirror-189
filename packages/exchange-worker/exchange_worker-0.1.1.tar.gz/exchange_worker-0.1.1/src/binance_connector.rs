use std::rc::Rc;
use std::sync::atomic::{AtomicBool, Ordering};

use binance::futures::websockets::*;
use binance::model::BookTickerEvent;

type Callback<'a> = dyn Fn(BookTickerEvent) -> ();

pub struct BinanceListenerOptions {
    tickers: Vec<String>,
    // market: FuturesMarket,
}

impl BinanceListenerOptions {
    pub fn new(tickers: Vec<String>) -> BinanceListenerOptions {
        Self { tickers }
    }
}

pub struct BinanceListener {
    token: Option<String>,
}

impl BinanceListener {
    pub fn new(token: Option<String>) -> BinanceListener {
        Self { token }
    }

    pub fn subscribe(&self, options: BinanceListenerOptions, handler: &Callback) {
        let keep_running = AtomicBool::new(true);
        handler(BookTickerEvent {
            update_id: 0,
            symbol: "".to_string(),
            best_bid: "".to_string(),
            best_bid_qty: "".to_string(),
            best_ask: "".to_string(),
            best_ask_qty: "".to_string(),
        });
        let mut callback_fn = |event: FuturesWebsocketEvent| {
            dbg!(&event);

            if let FuturesWebsocketEvent::BookTicker(e) = event {
                handler(e);
                // let nautilus_event: NautilusBookTickerEvent = e.into();
                // publish_to_redis_stream(&mut con, nautilus_event).unwrap_or_else(|e| { dbg!(&e); });
            }

            Ok(())
        };
        keep_running.swap(true, Ordering::Relaxed);

        let mut web_socket: FuturesWebSockets<'_> = FuturesWebSockets::new(&mut callback_fn);
        web_socket
            .connect_multiple_streams(&FuturesMarket::USDM, &options.tickers[..])
            .unwrap();

        if let Err(e) = web_socket.event_loop(&keep_running) {
            dbg!(&e);
            match e {
                err => {
                    println!("Error: {:?}", err);
                }
            }
        }
        web_socket.disconnect().unwrap();
    }
}


#[cfg(test)]
mod tests {
    #[test]
    fn some() {
        let list = vec![1, 2, 3];
        println!("Before defining closure: {:?}", list);

        let only_borrows = || println!("From closure: {:?}", list);

        println!("Before calling closure: {:?}", list);
        only_borrows();
        println!("After calling closure: {:?}", list);
    }
}