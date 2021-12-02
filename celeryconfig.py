enable_utc = True
timezone = "America/Toronto"

# Can only execute once per minute.
task_annotations = {
    'tasks.rss': {'rate_limit': '1/m'}
}