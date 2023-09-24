use cursive::align::HAlign;
use cursive::event::EventResult;
use cursive::traits::*;
use cursive::views::{Dialog, OnEventView, SelectView};
use cursive::Cursive;

pub fn show_log_file_list(siv: &mut Cursive)
{
    let mut select = SelectView::new()
        .h_align(HAlign::Center);

    select.add_all_str(vec!["test1", "test2"]);

    // select.set_on_submit(load_module);

    let select = OnEventView::new(select)
        .on_pre_event_inner('k', |s, _| {
            let cb = s.select_up(1);
            Some(EventResult::Consumed(Some(cb)))
        })
        .on_pre_event_inner('j', |s, _| {
            let cb = s.select_down(1);
            Some(EventResult::Consumed(Some(cb)))
        });

    siv.add_layer(
        Dialog::around(select.scrollable().fixed_size((30, 10))).title("EZSUP"),
    );
}
