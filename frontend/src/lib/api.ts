import axios from "axios";

const API_URL = import.meta.env.VITE_API_URL;

export const analyzeSentiment = async (text: string) => {
  try {
    const response = await axios.post(`${API_URL}/predict`, { text });
    if (response.status !== 200) {
      throw new Error("Failed to analyze sentiment");
    }
    return response.data;
  } catch (error) {
    if (axios.isAxiosError(error)) {
      console.error("Network error or API is down:", error);
    }

    console.error("Error analyzing sentiment:", error);
    throw error;
  }
};
