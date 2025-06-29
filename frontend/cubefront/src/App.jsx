import { Routes, Route } from "react-router-dom";
import Navbar from "./page/Navbar/Navbar";
import Home from "./page/Home/Home";

import Profile from "./page/Profile/Profile";
import Auth from "./page/Auth/Auth";
import TrackShipment from "./page/TrackShipment/TrackShipment";
import RouteAnomalies from "./page/RouteAnomalies/RouteAnomalies";
import PriceAnomalies from "./page/PriceAnomalies/PriceAnomalies";
function App() {
  return (
    <>
     
       <Navbar />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/PriceAnomalies" element={<PriceAnomalies />} />
        <Route path="/RouteAnomalies" element={<RouteAnomalies />} />
      
      
        <Route path="/TrackShipment" element={<TrackShipment />} />
        <Route path="/profile" element={<Profile />} />
    
        
      </Routes>
    </>
  );
}

export default App;
