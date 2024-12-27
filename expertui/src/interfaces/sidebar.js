import React, { useState } from 'react'

export default function Sidebar({changer}) {
  const [active , setactive]= useState(1)
  const mover=(x)=>{
    changer(x)
    if(x){
      setactive(1)

    }else{
      setactive(0)
    }
  }
  return (
    <div className='w-full pl-5 pt-6 bg-gray-100 px-7 h-screen text-black'>
      <div>
        <div className='text-2xl font-Nunito Sans font-bold relative -top-3 text-cyan-900 border-b-2 pb-2 border-gray-300'>Expert Courrier</div>
        
        <div className='text-xl font-zain  mt-1 -top-10 right-16'>
          <div className={`${active ===0 ? "border-cyan-900": "border-gray-100"} cursor-pointer  pl-2 py-1 my-1 border-l-2 pb-2  `} onClick={()=>mover(false)}>About</div>
          <div className={`${active ===1 ? "border-cyan-900": "border-gray-100"} cursor-pointer  pl-2 py-1 my-1 border-l-2 pb-2  `} onClick={()=>mover(true)}>Find</div>
        </div>

      </div>
    </div>
  )
}
