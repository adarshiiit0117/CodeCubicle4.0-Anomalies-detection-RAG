import React from 'react';
import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from "@/components/ui/table";

const TrackShipment = () => {
  const shipments = [
    {
      id: "SHP001",
      product_type: "Electronics",
      value: "$10,500",
      timestamp: "2025-06-29 10:34 AM",
    },
    {
      id: "SHP002",
      product_type: "Pharmaceutical",
      value: "$28,200",
      timestamp: "2025-06-28 03:20 PM",
    },
    {
      id: "SHP003",
      product_type: "Agricultural Tools",
      value: "$6,750",
      timestamp: "2025-06-27 08:10 AM",
    },
    {
      id: "SHP004",
      product_type: "Textiles",
      value: "$12,900",
      timestamp: "2025-06-26 06:45 PM",
    },
  ];

  return (
    <div className="min-h-screen bg-black p-5 pb-5 lg:p-20">
      <h1 className='font-bold text-3xl text-white'>Shipment Tracker</h1>
      <Table className="text-white border-x border-y mt-6">
        <TableHeader>
          <TableRow>
            <TableHead className="text-white">Shipment ID</TableHead>
            <TableHead className="text-white">Product Type</TableHead>
            <TableHead className="text-white">Value</TableHead>
            <TableHead className="text-white">Timestamp</TableHead>
          </TableRow>
        </TableHeader>
        <TableBody>
          {shipments.map((shipment) => (
            <TableRow key={shipment.id}>
              <TableCell className="text-white">{shipment.id}</TableCell>
              <TableCell className="text-white">{shipment.product_type}</TableCell>
              <TableCell className="text-white">{shipment.value}</TableCell>
              <TableCell className="text-white">{shipment.timestamp}</TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </div>
  );
};

export default TrackShipment;
