import React from "react";
import { Button } from "@/components/ui/button";
import { SheetClose } from "@/components/ui/sheet";
import {
  Home,
  LayoutDashboard,
  Bookmark,
  Activity,
  Banknote,
  Wallet,
  CreditCard,
  User,
  LogOut,
} from "lucide-react";
import { useNavigate } from "react-router-dom";

const menu = [
  { name: "Home", path: "/", icon: Home },
  { name: "Track Shipment", path: "/TrackShipment", icon: LayoutDashboard },
  { name: "Route Anomalies", path: "/RouteAnomalies", icon: Activity },
  { name: "Price Anomalies", path: "/PriceAnomalies", icon: Activity },
  { name: "Profile", path: "/profile", icon: User },
  { name: "Logout", path: "/", icon: LogOut },
];

const Sidebar = () => {
  const navigate = useNavigate();

  return (
    <div className="bg-blue-900 h-screen w-64 p-4 text-yellow-400 space-y-5 overflow-y-auto">
      {menu.map((item) => (
        <div key={item.name}>
          <SheetClose className="w-full">
            <Button
              variant="outline"
              className="flex items-center gap-5 py-4 w-full bg-blue-800 hover:bg-blue-700 border-blue-600 text-yellow-400"
              onClick={() => navigate(item.path)}
            >
              <span className="w-6 h-6">
                <item.icon className="w-full h-full text-yellow-400" />
              </span>
              <p className="text-yellow-400">{item.name}</p>
            </Button>
          </SheetClose>
        </div>
      ))}
    </div>
  );
};

export default Sidebar;
