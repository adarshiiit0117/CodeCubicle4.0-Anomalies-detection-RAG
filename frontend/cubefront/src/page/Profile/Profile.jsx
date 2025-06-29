import React from 'react';
import {
  Card,
  CardContent,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";
import { Button } from "@/components/ui/button";

const Profile = () => {
  const handleLogout = () => {
    console.log("Logging out...");
   
  };

  return (
    <div className='flex flex-col items-center mb-5 bg-black h-screen text-white'>
      <div className='pt-10 w-full lg:w-[60%]'>
        <Card className="bg-[#0f0f0f] text-white">
          <CardHeader className="pb-9">
            <CardTitle className='text-lg lg:text-xl'>My Information</CardTitle>
          </CardHeader>
          <CardContent>
            <div className='grid grid-cols-1 lg:grid-cols-2 gap-y-6 gap-x-20'>
              <div className='space-y-3'>
                <div className='flex'>
                  <p className='w-[9rem] font-semibold'>Email :</p>
                  <p className='text-gray-400'>aditya.karn@example.com</p>
                </div>
                <div className='flex'>
                  <p className='w-[9rem] font-semibold'>Full Name :</p>
                  <p className='text-gray-400'>Aditya Karn</p>
                </div>
                <div className='flex'>
                  <p className='w-[9rem] font-semibold'>Type :</p>
                  <p className='text-gray-400'>Admin</p>
                </div>
                <div className='flex'>
                  <p className='w-[9rem] font-semibold'>Role :</p>
                  <p className='text-gray-400'>Warehouse Manager</p>
                </div>
              </div>
              <div className='space-y-3'>
                <div className='flex'>
                  <p className='w-[9rem] font-semibold'>Address :</p>
                  <p className='text-gray-400'>Patna</p>
                </div>
                <div className='flex'>
                  <p className='w-[9rem] font-semibold'>City :</p>
                  <p className='text-gray-400'>Patna</p>
                </div>
                <div className='flex'>
                  <p className='w-[9rem] font-semibold'>Postcode :</p>
                  <p className='text-gray-400'>800001</p>
                </div>
                <div className='flex'>
                  <p className='w-[9rem] font-semibold'>Country :</p>
                  <p className='text-gray-400'>India</p>
                </div>
              </div>
            </div>
          </CardContent>
        </Card>

     
        <div className="mt-6 flex justify-center">
          <Button onClick={handleLogout} className="bg-red-600 hover:bg-red-700 text-white px-6 py-2 rounded-md">
            Log Out
          </Button>
        </div>
      </div>
    </div>
  );
};

export default Profile;
