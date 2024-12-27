
import React, { useState } from "react";
import Sidebar from "./interfaces/sidebar";
import Find from "./interfaces/find";
import About from "./interfaces/about";

function App() {
  const [current , setcurrent] = useState(true)
  const changer =(K)=>{
    setcurrent(K)
  }
  return (
    <div className="App">
      <div className="fixed top-0">
        <Sidebar changer = {changer}/>
      </div>
      <div className={`${!current && "scale-0"} top-5 mx-8 w-cw86 absolute left-52 duration-300`}>
        <Find />
      </div>
      <div className={`${current && "scale-0"} top-5 mx-8 w-cw86 absolute left-52 duration-300`}>
        <About />
      </div>

    </div>
  );
}

export default App;
