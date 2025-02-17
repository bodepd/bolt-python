---
title: Acknowledging requests
lang: en
slug: acknowledge
order: 7
---

<div class="section-content">

Actions, commands, and options requests must **always** be acknowledged using the `ack()` function. This lets Slack know that the request was received and updates the Slack user interface accordingly.

Depending on the type of request, your acknowledgement may be different. For example, when acknowledging a menu selection associated with an external data source, you would call `ack()` with a list of relevant [options](https://api.slack.com/reference/block-kit/composition-objects#option).

We recommend calling `ack()` right away before sending a new message or fetching information from your database since you only have 3 seconds to respond.

</div>

<div>
<span class="annotation">Refer to <a href="https://slack.dev/bolt-python/api-docs/slack_bolt/kwargs_injection/args.html" target="_blank">the module document</a> to learn the available listener arguments.</span>
```python
# Example of responding to an external_select options request
@app.options("menu_selection")
def show_menu_options(ack):
    options = [
        {
            "text": {"type": "plain_text", "text": "Option 1"},
            "value": "1-1",
        },
        {
            "text": {"type": "plain_text", "text": "Option 2"},
            "value": "1-2",
        },
    ]
    ack(options=options)
```
</div>