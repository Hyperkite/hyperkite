function poll_trials(init, interval) {
    // Recursive function updates number of trials (n_trials) from server
    // every 'interval' milliseconds and reloads page if number is different.
    setTimeout(function(){
        $.ajax({ url: "/api/n_trials", success: function(data) {
            if (data != init) {
                location.reload();
            }
            poll_trials(init, interval);
        }, dataType: "json"});
    }, interval);
}
