import React, { useState, useEffect } from "react";
import PlantList from "./PlantList";

export default function App() {
  const [plants, setPlants] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetch("http://127.0.0.1:8000/plants/") // آدرس API بک‌اند
      .then((res) => {
        if (!res.ok) {
          throw new Error("خطا در دریافت داده‌ها");
        }
        return res.json();
      })
      .then((data) => {
        setPlants(data);
        setLoading(false);
      })
      .catch((err) => {
        setError(err.message);
        setLoading(false);
      });
  }, []);

  if (loading) return <p>در حال بارگذاری...</p>;
  if (error) return <p>خطا: {error}</p>;

  return <PlantList plants={plants} />;
}
