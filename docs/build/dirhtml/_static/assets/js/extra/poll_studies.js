function poll_studies(init, interval) {
    // Recursive function updates number of studies (n_studies) from server
    // every 'interval' milliseconds and reloads page if number is different.
    setTimeout(function(){
        $.ajax({ url: "/api/n_studies", success: function(data) {
            if (data != init) {
                location.reload();
            }
            poll_studies(init, interval);
        }, dataType: "json"});
    }, interval);
}


