
function handleRequests(number) {
    var url = '';
    var urls;
    while(number > 0){
        urls.push(url);
        --number;
    }
    
    var data = Promise.all(urls.map(url=>fetch(url))).then(response => {
        if (response.ok) {
            return response.json();
        } else {
            return Promise.reject(response.status);
        }
    })
    .catch(err => console.log(`Error with message: ${err}`));


}