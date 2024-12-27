import React, { useState } from 'react'
import axios from 'axios'


export default function Find() {
  const root = "http://127.0.0.1:5000"
  const [src, setsrc] = useState("D")
  const [des, setdes] = useState("D")
  const [consider, setconsider] = useState("0")
  const [Opath, setOpath] = useState(["Path will appear Here"])

  const [subpath, setsubpath] = useState([[[" "], " "], [["Discover Subpaths"], 0, 0]])
  const [discov , setdiscov]= useState(false)


  const [ecost, setecost] = useState(0)
  const [etime, setetime] = useState(0)

  const [currentIndex, setCurrentIndex] = useState(1);
  const currentPath = Opath[currentIndex] || [];  // Fallback to an empty array if the current path is undefined
  const [path, cost, time] = currentPath
  const [traversalDis , setTraversaldis] = useState([])

  let text = "Cost"
  if (consider == "0") {
    text = "Cost"
  }
  else if (consider == "1") {
    text = "Time"
  }
  else if (consider == "2") {
    text = "Optimal"
  }
  const GettingPaths = async () => {
    try {
      const end = "/getPaths"
      const res = await axios.post(root + end, { "src": src, "des": des, "con": consider }, {
        headers: {
          "Content-Type": "application/json",
        }
      })
      const response = res.data
      setdiscov(false)
      setecost(response.cost)
      setetime(response.time)
      setOpath(response.paths)
      //alert(response.paths[1])
    } catch (e) {
      alert(e)
    }
  }




  const alterpaths = async () => {

    try {
      const end = "/alterpaths"
      const res = await axios.post(root + end, { "src": src, "des": des, "con": consider }, {
        headers: {
          "Content-Type": "application/json",
        }
      })
      setdiscov(!discov)
      const response = res.data
      //setecost(response.cost)
      //setetime(response.time)
      setsubpath(response.paths)
      //alert(response.paths[0][1])
    } catch (e) {
      alert(e)
    }

  }








  const handleNext = (k) => {
    const len = subpath.length


    if(k==1){
      if (currentIndex + 1 < len)
        setCurrentIndex(currentIndex + 1);  // Move to the next path
      else {
        setCurrentIndex(1)
      }
    }else if(k===0){
      if (currentIndex-1 >=1)
        setCurrentIndex(currentIndex - 1);  // Move to the next path
      else {
        setCurrentIndex(len-1)
      }
    }
  };


  
  const explain = async () => {
    try {
      const end = "/explain_Path"
      const res = await axios.post(root + end, { "src": src, "des": des, "con": consider }, {
        headers: {
          "Content-Type": "application/json",
        }
      })
      const response = res.data
      setdiscov(false)
      setTraversaldis(response.paths)
      //alert(response.paths[1])
    } catch (e) {
      alert(e)
    }
  }


  return (
    <div className='w-full pb-12'>
      <div className=' mt-0 px-3 pt-3 pb-6 bg-cyan-900 rounded-lg shadow-md shadow-gray-400'>
        <div className='font-Nunito Sans text-2xl mb-5  py-1 text-white px-6 rounded-md'>Define Your journey</div>


        <div className='px-6 '>
          <table className=' w-full'>
            <tr>
              <td>
                <span className='text-lg text-white  pr-5'>Source :</span>
                <select id="dropdown" className="border  border-none rounded-s-md p-2 w-52 px-5" value={src} onChange={(e) => { setsrc(e.target.value) }}>
                  <option value="D">Africa</option>
                  <option value="E">Amarica</option>
                  <option value="F">Arab</option>
                  <option value="C">Australia</option>
                  <option value="B">China</option>
                  <option value="H">England</option>
                  <option value="G">France</option>

                  <option value="I">Italy</option>
                  <option value="A">Sri Lanka</option>

                </select>
              </td>
              <td className='pl-10'>
                <span className='text-lg text-white pr-5'>Destination :</span>
                <select id="dropdown" className="border rounded-s-md p-2 w-52 px-5" value={des} onChange={(e) => { setdes(e.target.value) }}>
                  <option value="D">Africa</option>
                  <option value="E">Amarica</option>
                  <option value="F">Arab</option>
                  <option value="C">Australia</option>
                  <option value="B">China</option>
                  <option value="H">England</option>
                  <option value="G">France</option>

                  <option value="I">Italy</option>
                  <option value="A">Sri Lanka</option>

                </select>
              </td>
              <td className='pl-10'>
                <span className='text-lg text-white pr-5'>Consideration</span>
                <select id="dropdown" className="border rounded p-2 w-52  px-5" value={consider} onChange={(e) => { setconsider(e.target.value) }} >
                  <option value="0">Minimum Cost</option>
                  <option value="1">Minimum Time</option>
                  <option value="2">Optimal</option>

                
                </select>
              </td>
              <td className='pl-32'><div className='ml-5 py-2 px-10 text-black bg-green-500 shadow-md shadow-gray-600 w-fit hover:scale-105 duration-200 hover:bg-green-400 cursor-pointer rounded-lg font-bold' onClick={GettingPaths}>Find Route</div></td>

            </tr>
          </table>
        </div>
      </div>
      


      <div className='border-gray-200 shadow-sm shadow-gray-200 border-2 py-3 pb-6 px-3 mt-5 rounded-lg relative h-auto duration-300'>

        <div className='py-2 font-Nunito Sans  text-2xl w-full  text-black px-5 font-semibold rounded-lg'>Path With Respect to {text}</div>
        <div className=' ml-5 mt-8 relative'>
          {(() => {
            const arr = []
            let i = 0

            for (i = 0; i < Opath.length; i++) {
              arr.push(
                <span>
                  <span className='text-2xl font-bold'>-----{">"}</span>
                  <span className="px-8 py-2 text-xl bg-green-500 rounded-md text-white mr-5">{Opath[i]}</span>
                </span>



              )
            }
            return arr
          })()}


          <div className=' absolute right-3 w-60 -top-20 bg-cyan-900 px-5 py-5 rounded-lg z-30'>
            <div className={`${consider === "0" ? "font-bold  text-2xl text-white border-l-4 border-green-500" : "font-normal text-white text-2xl"} py-1 pl-5 duration-100`}>Cost : {ecost}$</div>
            <div className={`${consider === "1" ? "font-bold  text-2xl text-white border-l-4 border-green-500" : "font-normal text-white text-2xl"} py-1 pl-5 duration-100`}>Time : {etime} days</div>
            <div className='mt-2 py-2 text-center text-md rounded-md text-black font-Nunito Sans font-semibold bg-green-500 w-full hover:scale-105 duration-200 hover:bg-green-400 cursor-pointer' onClick={explain}>Explain Path</div>
          </div>


          

        </div>
        <div className='mx-12 py-5 text-gray-600 duration-300'>
      {traversalDis.map((step, index) => (
        <div
          key={index}
          dangerouslySetInnerHTML={{ __html: step }}
          style={{ marginBottom: "1em" }}
        />
      ))}
      </div>
      </div>





      

      
      








      <div className='border-gray-200 shadow-sm shadow-gray-200 border-2 mt-3 px-3 py-3 rounded-lg'>

        <div className='text-black  py-2 px-3 relative rounded-md'>
          <div className='text-2xl font-semibold'> Discover Alternative Solutions</div>
          <div className='py-2 px-10 text-black font-Nunito Sans bg-green-500 w-fit hover:scale-105 duration-200 hover:bg-green-400 cursor-pointer rounded-lg font-semibold absolute top-1 right-3' onClick={alterpaths}>Retrieve Alter Paths</div>
        </div>


        <div className={`${!discov && "scale-0"} duration-300 mt-5`}>

          <div className='py-3 rounded-md  text-xl font-bold pl-7 text-white bg-cyan-900  shadow-sm shadow-gray-400 mb-4'>
            <span className='pr-60 '>Alternative path: {currentIndex}/{subpath.length-1}</span>
            <span className='px-60 '>Cost : {subpath[currentIndex][1]} $</span>
            <span className='px-20 '>Duration : {subpath[currentIndex][2]} Days</span>
          </div>
          <div className='ml-5   mt-10'>
          {(() => {
            const arr = []
            let i = 0

            for (i = 0; i < subpath[currentIndex][0].length; i++) {
              arr.push(
                <span>
                  <span className='text-2xl font-bold'>-----{">"}</span>
                  <span className="px-8 py-2 text-xl bg-black rounded-md text-white mr-5">{subpath[currentIndex][0][i]}</span>
                </span>



              )
            }
            return arr
          })()}
          </div>
          <div className='mt-12'>
            
          </div>






          <div className='ml-12'>
          <div onClick={()=>handleNext(0)} className=" w-fit mt-12 px-16 py-2 bg-green-500 text-white rounded-md hover:scale-105 duration-200 cursor-pointer inline-block mr-3">Prev</div>
          <div onClick={()=>handleNext(1)} className=" w-fit mt-12 px-16 py-2 bg-green-500 text-white rounded-md hover:scale-105 duration-200 cursor-pointer inline-block">Next</div>
          </div>
        </div>

      </div>
    </div>
  )
}
