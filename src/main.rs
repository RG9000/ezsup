use cursive::align::HAlign;
use cursive::event::EventResult;
use cursive::traits::*;
use cursive::views::{Dialog, OnEventView, SelectView};
use cursive::Cursive;

mod tar;

fn main() {
    let mut select = SelectView::new()
        .h_align(HAlign::Center)
        .autojump();

    select.add_all_str(vec!["Tar up log files", "Quit"]);

    // Sets the callback for when "Enter" is pressed.
    select.set_on_submit(load_module);

    // Let's override the `j` and `k` keys for navigation
    let select = OnEventView::new(select)
        .on_pre_event_inner('k', |s, _| {
            let cb = s.select_up(1);
            Some(EventResult::Consumed(Some(cb)))
        })
        .on_pre_event_inner('j', |s, _| {
            let cb = s.select_down(1);
            Some(EventResult::Consumed(Some(cb)))
        });

    let mut siv = cursive::default();

    siv.add_layer(
        Dialog::around(select.scrollable().fixed_size((30, 10))).title("EZSUP"),
    );

    siv.run();
}

// Let's put the callback in a separate function to keep it clean,
// but it's not required.
fn load_module(siv: &mut Cursive, option: &str) {
    match option {
        "Tar up log files" => {
            tar::show_log_file_list(siv);
        }
        "Quit" => {
            siv.quit();
        }
        _ => {}
    }
}
