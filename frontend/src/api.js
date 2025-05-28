import axios from "axios";

const API_BASE_URL = "http://127.0.0.1:8000/";

export const fetchPlants = async () => {
  const response = await axios.get(`${API_BASE_URL}plants/`);
  return response.data;
};
