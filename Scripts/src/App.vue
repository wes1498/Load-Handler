<template>
  <div id="app">
    <div class="main-panel">
        <div class="header">
            <h2> TRANSACTION LOAD MANAGER </h2>
        </div>

        <div class="content">
            <div class="top-panel">
            </div>
            <div class="bottom-panel">
                <div class="indiv-panel">
                    Adjust Settings
                    <br />
                    <div class="col1">

                        <label> <div class = "form-title">Set Transaction Rate: </div></label>
                        <br />
                        <input v-model="transaction_rate" id = transaction_rate type="number"/>
                        <br /><br />
                        <input id="submit-button" type="submit" value="Submit" v-on:click="handleRequests(transaction_rate)">

                      </div>

                </div>
                <div class="indiv-panel">  <div id="display_rate">Current Transaction <br />Rate: <br /><span class="rate"></span></div>
              

                </div>
                <div class="indiv-panel">Output Log
                <br />
                  <div class="output-text" v-for="output in this.outputs">
                    {{output}} <br />
                  </div></div>
            </div>
        </div>
    </div>
  </div>
</template>

<script>

export default {
  name: 'app',
  data () {
    return {
      outputs: [],
      transaction_rate: null,
    }
  },
  methods: {
    handleRequests : function(number) {
      const proxyUrl = "https://cors-anywhere.herokuapp.com/";
      var url = 'http://test-lb-1235939263.us-west-2.elb.amazonaws.com/loadBalancer';
      var urls = [];
      var requests = number;
      while(requests > 0){
          urls.push(proxyUrl + url);
          --requests;
      }
      document.getElementsByClassName('rate')[0].innerText = number

      Promise.all(urls.map(url=>fetch(url).then(response => {

          if (response.ok) {
              var date = new Date();
              this.outputs.push("Transaction: " + Math.random().toString(36).substring(7) + " " + date.toLocaleTimeString());

          } else {
              return Promise.reject(response.status);
          }
      })));
    }
  }
}
</script>

<style>
body {
    margin: 0;
    font-family: "Poppins", sans-serif;
    font-size: 0.875rem;
    font-weight: 400;
    line-height: 1.5;
    color: #525f7f;
    text-align: left;
    background-color: #1e1e2f;
    height: 100%;
    max-height: 100%;
    overflow-y: hidden;
}

.header {
    margin-left: 2rem;
    padding-top: .3125rem;
    padding-bottom: .3125rem;
    color: #ffffff;
    margin-left: 17px;
    margin-top: 3px;
    text-transform: uppercase;
    font-size: 1rem;
}

.main-panel {
    position: relative;
    min-height: 100vh;
    border-top: 5px solid #e14eca;
    background: linear-gradient(#1e1e2f, #1e1e24);
    width: 100%;
    color: (255, 255, 255, .7);
}

.content {
    width: 100%;
    margin-left: auto;
    margin-right: auto;
    display: flex;
    flex-wrap: wrap;
    flex-direction: column;
    justify-content: space-between
}

.top-panel {
    background-color: #27293d;
    border-radius: 5px;
    height: 250px;
    width: 80%;
    align-items: center;
    margin-left: auto;
    margin-right: auto;
    position: relative;
}

.bottom-panel {
    width: 80%;
    margin-left: auto;
    margin-right: auto;
    align-items: center;
    display: flex;
    margin-top: 2%;
}

.indiv-panel {
    background-color: #27293d;
    border-radius: 5px;
    padding: 10px;
    width: 100%;
    height: 180px;
    word-wrap:break-word;
    position: relative;
    overflow-y: scroll;
    overflow-x: hidden;

}

.indiv-panel:nth-child(2) {
    margin-left: 10px;
    margin-right: 10px;
}

#transaction_rate {
    padding: 10px 10px;
    box-sizing: border-box;
    font-size: .9em;
    width: 80%;
}

input[type=submit] {
    background-color: #e14eca;
    border: none;
    color: white;
    padding: 10px 10px;
    text-align: center;
    text-decoration: none;
    display: inline-block;
    font-size: .9em;
    border-radius: 3px;
    text-transform: uppercase;
    margin-top: -15px;
}

.form-title {
    color: #fff;
}

#display_rate {
    color: #fff;
    font-size: 1em;
    position: relative;
    word-wrap: break-word;
  }

  #output {
      color: #fff;
      font-size: 1em;
      position: relative;
      word-wrap: break-word;
    }

.rate {
    float: right;
    font-size: 2em;
    font-weight: bolder;
}

form {
    width: 40%;
}

.col1 {
    display: -webkit-inline-box;
    flex-direction: column;
}

.output-text {
    overflow-y: scroll;
    position: inherit;

    display: contents;
    height: 130px;
    color: #fff;
    font-size: .8em;
}
</style>
