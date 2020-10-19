import React ,{Component}from 'react';
import './App.css';
import axios from 'axios';

import './App.css';
import Background from './bg.jpg';

const divStyle = {
  width: '100%',
  height: '1000px',
  backgroundImage: `url(${Background})`,
  backgroundSize: 'cover',
  backgroundrepeat: 'no-repeat'
};

const divStyle2 = {
  color: 'white',
};

class App extends Component{

  state = {
    searchText:null,
    searchresults :[],
  }

  updateInputValue(evt) {
    this.setState({
      searchText: evt.target.value
    });
  }


  onSubmit(evt) {

    console.log("Radhesh");
    const data = {data : this.state.searchText};
    axios.post(`http://127.0.0.1:5000/`,data)
    .then(res => {this.setState( {searchresults: res["data"]["answer"]})})

    console.log(this.state);

  }


  render(){
      return (
      <div style={divStyle}>
        <title>CC Searcher</title>
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" integrity="sha384-JcKb8q3iqJ61gNV9KGb8thSsNjpSL0n8PARn9HuZOnIxN0hoP+VmmDGMN5t9UJ0Z" crossOrigin="anonymous" />
        <style dangerouslySetInnerHTML={{__html: "\n    body {\n        background-image:  url('bg.jpg') ;\n        background-repeat: no-repeat;\n        background-attachment: fixed;\n        background-color: lightblue;\n        background-size: cover;\n        font-family: \"Georgia\";\n    }\n    form{\n        text-align:center;\n        margin: 30px 30px 30px 30px;\n        font-family: bold;\n        font-size:1 em;\n    }\n    p{\n        text-align:center;\n        font-size: 1.2em;\n    }\n    " }} />
        <h3 style={{textAlign: 'center', color: 'green', margin: '40px'}}> Welcome to Codeforces Search Engine </h3>
        <br/>
        <form value = {this.state.searchText} onChange={evt => this.updateInputValue(evt)}>
          <input className="col-9 form-group" type="text" placeholder="Enter topic/contest rating...."/>
          <input value = "Submit" onClick = {evt => this.onSubmit(evt)} className="btn-secondary " />
        </form>
        <br/>


<table style = {divStyle2}> 
  <tr>
    <th>Numb</th>
    <th>File Name</th>
  </tr>

      {this.state.searchresults.map((item,index) => (
        <tr>
          <td>{index+1}</td>
          <td>{item}</td>
        </tr>
      ))}
  </table>
      </div>
    );
  }
}

export default App;
