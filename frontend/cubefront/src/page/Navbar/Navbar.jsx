import React from "react";
import {
  Sheet,
  SheetContent,
  SheetHeader,
  SheetTrigger,
} from "@/components/ui/sheet";

import { Menu } from "lucide-react";
import { Avatar, AvatarImage ,AvatarFallback} from "@/components/ui/avatar";
import { Button } from "@/components/ui/button";
import Sidebar from "./Sidebar"; 
import { Search } from 'lucide-react';

const Navbar = () => {
  return (
    <div className="px-2 py-3 border-b z-50 bg-black sticky top-0 left-0 right-0 flex justify-between items-center">
      <div className="flex items-center gap-3">
        <Sheet>
          <SheetTrigger>
            <Button variant="ghost" size="icon" className="rounded-full h-11 w-11">
              <Menu className="h-7 w-7 text-white" />
            </Button>
          </SheetTrigger>

          <SheetContent
            className="w-72 bg-black text-white border-r-2 flex flex-col justify-between pt-2"
            side="left"
          >
            <SheetHeader className="p-0">
              <div className="flex justify-center items-center gap-3">
                
                <div>
                  <span className="font-bold text-red-500 text-xl">Logistics Pulse Copilot</span>
                </div>
              </div>
            </SheetHeader>
            <Sidebar />
          </SheetContent>
        </Sheet>
        <p className="text-3xl lg:text-base cursor-pointer text-red-700">
          Logistics Pulse Copilot
          <br/> <p className="text-sm lg:text-base cursor-pointer text-white">Monitor Detect Act</p>
        </p>
       
        <div className="p-0 ml-9">
          <Button  variant='outline'className='w-250 h-10'>
           <Search className="w-5 h-5 text-grey-700" />

            <span>Search</span>
          </Button>

        </div>
      </div>
      <div>
        <Avatar>
          <AvatarFallback>
            A
          </AvatarFallback>
        </Avatar>
      </div>
    </div>
  );
};

export default Navbar;
