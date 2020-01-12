function handleRequests(number) {
    var url = 'http://test-lb-1235939263.us-west-2.elb.amazonaws.com/loadBalancer';
    var urls = [];
    while(number > 0){
        urls.push(url);
        --number;
    }

    Promise.all(urls.map(url=>fetch(url).then(response => {
        if (response.ok) {
            response.json().then(data => ({status: response.status, body:data})).then(obj => console.log(obj)));
        } else {

            return Promise.reject(response.status);
        }
    })));
}


function output(txt) {
  var jsonStr = JSON.stringify(txt);
  document.getElementById('output').innerText = jsonStr;
}
