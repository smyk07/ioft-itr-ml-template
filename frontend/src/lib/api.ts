const API_URL = import.meta.env.PUBLIC_API_URL || "http://localhost:8000";

export async function predict(data: any) {
  const response = await fetch(`${API_URL}/predict`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(data),
  });

  return await response.json();
}
