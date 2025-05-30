import React, { useEffect, useState } from "react";
import styles from "./PlantList.module.css";
import { fetchPlants, fetchPlantHealth } from "./api";

export default function PlantList() {
  const [plants, setPlants] = useState([]);
  const [plantsHealth, setPlantsHealth] = useState([]);

  useEffect(() => {
    const getPlants = async () => {
      try {
        const data = await fetchPlants();
        setPlants(data);
      } catch (error) {
        console.error("خطا در دریافت گیاهان:", error);
      }
    };

    getPlants();
  }, []);

  useEffect(() => {
        const getPlantsHealth = async () => {
      try {
        const data = await fetchPlantHealth();
        setPlantsHealth(data);
      } catch (error) {
        console.error("خطا در دریافت گیاهان:", error);
      }
    };

    getPlantsHealth();
  },[])

  return (
    <div className={styles.pageContainer}>
      {/* 👇 هدر جدید */}
      <header className={styles.header}>
        <div className={styles.logo}>🌱 PlantMonitor</div>
        <nav className={styles.nav}>
          <a href="#">Home</a>
          <a href="#">Plants</a>
          <a href="#">About us</a>
        </nav>
      </header>

      <main className={styles.mainContent}>
        <h1 className={styles.pageTitle}>List of plants</h1>
        <ul className={styles.plantGrid}>
          {plants.map((plant) => {
            const plantStat = plantsHealth.find(item => item.plant == plant.id)
            
            return (
            <li key={plant.id} className={styles.plantCard}>
              <h2>{plant.name}</h2>
              <p>
                <b>Species:</b> {plant.species}
              </p>
              <p>
                <b>Watering Interval (days):</b> {plant.waterInterval}
              </p>
              <p>
                <b>Temperature Range (°C):</b> {plant.tempRange}
              </p>
              <p>
                <b>Temperature (°C):</b> {plantStat.temperature}
              </p>
              <p>
                <b>Soil Moist:</b> {plantStat.moisture}
              </p>
              <p>
                <b>humidity:</b> {plantStat.humidity}
              </p>
            </li>
          )})}
        </ul>
      </main>
    </div>
  );
}
