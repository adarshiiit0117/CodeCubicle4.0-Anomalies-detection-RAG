import React from 'react';
import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from "@/components/ui/table";

const PriceAnomalies = () => {
  const shipments = [
    {
      shipment_id: "SHP1001",
      product_type: "Electronics",
      value: "₹12,500",
      timestamp: "2025-06-28 14:12:45",
      is_anomaly: true,
      price_deviation: "₹2,100",
    },
    {
      shipment_id: "SHP1002",
      product_type: "Pharmaceutical",
      value: "₹7,800",
      timestamp: "2025-06-28 16:32:10",
      is_anomaly: true,
      price_deviation: "₹1,250",
    },
    {
      shipment_id: "SHP1003",
      product_type: "Textiles",
      value: "₹15,200",
      timestamp: "2025-06-27 10:55:30",
      is_anomaly: true,
      price_deviation: "₹3,600",
    },
    {
      shipment_id: "SHP1004",
      product_type: "Agricultural Tools",
      value: "₹9,300",
      timestamp: "2025-06-27 19:20:05",
      is_anomaly: true,
      price_deviation: "₹1,800",
    },
  ];

  return (
    <div className="min-h-screen bg-black p-5 pb-5 lg:p-20">
      <h1 className='font-bold text-3xl text-white'>Price Anomalies</h1>
      <Table className="text-white border-x border-y mt-6">
        <TableHeader>
          <TableRow>
            <TableHead className="text-white">Shipment ID</TableHead>
            <TableHead className="text-white">Product Type</TableHead>
            <TableHead className="text-white">Value</TableHead>
            <TableHead className="text-white">Timestamp</TableHead>
            <TableHead className="text-white">Is Anomaly</TableHead>
            <TableHead className="text-white text-right">Deviation (₹)</TableHead>
          </TableRow>
        </TableHeader>
        <TableBody>
          {shipments.map((shipment) => (
            <TableRow key={shipment.shipment_id}>
              <TableCell className="text-white">{shipment.shipment_id}</TableCell>
              <TableCell className="text-white">{shipment.product_type}</TableCell>
              <TableCell className="text-white">{shipment.value}</TableCell>
              <TableCell className="text-white">{shipment.timestamp}</TableCell>
              <TableCell className="text-white">
                {shipment.is_anomaly ? "Yes" : "No"}
              </TableCell>
              <TableCell className="text-right text-white">{shipment.price_deviation}</TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </div>
  );
};

export default PriceAnomalies;
