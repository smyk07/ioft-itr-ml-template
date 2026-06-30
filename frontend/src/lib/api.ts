const API_URL = import.meta.env.PUBLIC_API_URL || "http://localhost:8000";

/** Matches backend schemas.PredictRequest */
export interface PredictRequest {
  x: number;
}

/** Matches backend schemas.PredictResponse */
export interface PredictResponse {
  prediction: number;
  confidence: number;
}

/** GET /health — warm-up / availability check */
export async function health(): Promise<{ status: string }> {
  const response = await fetch(`${API_URL}/health`);
  if (!response.ok) {
    throw new Error("Health check failed");
  }
  return response.json();
}

/** POST /predict — run inference */
export async function predict(data: PredictRequest): Promise<PredictResponse> {
  const response = await fetch(`${API_URL}/predict`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data),
  });
  if (!response.ok) {
    throw new Error(`Prediction failed: ${response.statusText}`);
  }
  return response.json();
}
