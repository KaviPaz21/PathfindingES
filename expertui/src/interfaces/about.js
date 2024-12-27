import React from 'react'
import MAP from "../img/map.jpg"

export default function About() {
  return (
    <div>
        <h1 className='font-Nunito Sans font-bold text-2xl text-white py-3 px-5 rounded-md w-full bg-cyan-900'>Expert Courrier - Courrier Pathfinding Expert System</h1>
        <img src={MAP} alt="msp" className='w-cw70' />

        <div className='border-gray-200 shadow-sm shadow-gray-200 border-2 py-3 rounded-lg px-5 my-5'>
            <div className='text-2xl font-Nunito Sans font-bold py-3'>Objectives</div>
            <div className='text-lg px-5'>
                Determine the paths with respect to client considerations.
                <div className='ml-20 py-4'>
                    <ul>
                        <li>Minimum Cost</li>
                        <li>Minimum Time</li>
                        <li>Optimal Cost And Time</li>
                    </ul>
                </div>
            </div>

        </div>
        <div className='border-gray-200 shadow-sm shadow-gray-200 border-2 py-3 rounded-lg px-5 my-5'>
            <div className='text-2xl font-Nunito Sans font-bold py-3'> Toolkit - Experta</div>
            
        </div>

        <div className='border-gray-200 shadow-sm shadow-gray-200 border-2 py-3 rounded-lg px-5'>
            <div className='text-2xl font-Nunito Sans font-bold py-3'> Featues</div>
            <div className='text-lg px-5'>
                System Will facilitate following features
                <div className='ml-20 py-4 text-xl font-semibold'>
                    <ul>
                        <li>Handle Null and incorrect Inputs</li>
                        <li>Provide best solution</li>
                        <li>Explain the Solutions</li>
                        <li>Gives Alternative solutions</li>
                    </ul>
                </div>
            </div>
            
        </div>
    </div>
  )
}
