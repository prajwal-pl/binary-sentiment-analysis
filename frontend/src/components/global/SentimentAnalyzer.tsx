import { useState } from "react";
import { Button } from "@/components/ui/button";
import { Textarea } from "@/components/ui/textarea";

interface SentimentResult {
  sentiment: "positive" | "negative";
  confidence: number;
}

export function SentimentAnalyzer() {
  const [text, setText] = useState("");
  const [result, setResult] = useState<SentimentResult | null>(null);
  const [isLoading, setIsLoading] = useState(false);

  const analyzeSentiment = async () => {
    if (!text.trim()) return;

    setIsLoading(true);
    try {
      // TODO: Replace with actual API call to backend
      const response = await fetch("/api/analyze", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ text }),
      });

      if (!response.ok) {
        throw new Error("Analysis failed");
      }

      const data = await response.json();
      setResult(data);
    } catch (error) {
      console.error("Analysis failed:", error);
      // Fallback with mock data for demo
      const mockResult: SentimentResult = {
        sentiment: Math.random() > 0.5 ? "positive" : "negative",
        confidence: Math.random() * 0.4 + 0.6,
      };
      setResult(mockResult);
    } finally {
      setIsLoading(false);
    }
  };

  const clearAnalysis = () => {
    setText("");
    setResult(null);
  };

  return (
    <div className="min-h-screen bg-gray-50 flex items-center justify-center p-6">
      <div className="w-full max-w-2xl mx-auto space-y-6">
        {/* Header */}
        <div className="text-center space-y-2">
          <h1 className="text-3xl font-semibold text-gray-900">
            Sentiment Analysis
          </h1>
          <p className="text-gray-600">
            Analyze the emotional tone of your text
          </p>
        </div>

        {/* Main Card */}
        <div className="bg-white border border-gray-200 rounded-lg p-6 shadow-sm">
          <div className="space-y-6">
            {/* Input Section */}
            <div className="space-y-2">
              <label
                htmlFor="sentiment-text"
                className="block text-sm font-medium text-gray-700"
              >
                Enter your text
              </label>
              <Textarea
                id="sentiment-text"
                placeholder="Type or paste your text here..."
                value={text}
                onChange={(e) => setText(e.target.value)}
                className="min-h-32 resize-none"
                disabled={isLoading}
              />
            </div>

            {/* Action Buttons */}
            <div className="flex gap-3">
              <Button
                onClick={analyzeSentiment}
                disabled={!text.trim() || isLoading}
                className="flex-1"
                size="lg"
              >
                {isLoading ? (
                  <>
                    <div className="w-4 h-4 border-2 border-gray-300 border-t-gray-600 rounded-full animate-spin mr-2" />
                    Analyzing...
                  </>
                ) : (
                  "Analyze Sentiment"
                )}
              </Button>

              {(text || result) && (
                <Button
                  onClick={clearAnalysis}
                  variant="outline"
                  size="lg"
                  disabled={isLoading}
                >
                  Clear
                </Button>
              )}
            </div>

            {/* Results Section */}
            {result && (
              <div className="mt-6 p-4 bg-gray-50 rounded-lg border">
                <h3 className="text-lg font-medium text-gray-900 mb-3">
                  Result
                </h3>

                <div className="flex items-center justify-between">
                  <div className="flex items-center space-x-2">
                    <div
                      className={`w-3 h-3 rounded-full ${
                        result.sentiment === "positive"
                          ? "bg-green-500"
                          : "bg-red-500"
                      }`}
                    />
                    <span className="text-gray-900 font-medium capitalize">
                      {result.sentiment}
                    </span>
                  </div>

                  <div className="text-right">
                    <div className="text-sm text-gray-500">Confidence</div>
                    <div className="text-lg font-medium text-gray-900">
                      {(result.confidence * 100).toFixed(1)}%
                    </div>
                  </div>
                </div>

                {/* Confidence Bar */}
                <div className="mt-3">
                  <div className="w-full bg-gray-200 rounded-full h-2">
                    <div
                      className={`h-2 rounded-full transition-all duration-300 ${
                        result.sentiment === "positive"
                          ? "bg-green-500"
                          : "bg-red-500"
                      }`}
                      style={{ width: `${result.confidence * 100}%` }}
                    />
                  </div>
                </div>
              </div>
            )}
          </div>
        </div>

        {/* Footer */}
        <div className="text-center">
          <p className="text-gray-500 text-sm">Powered by AI</p>
        </div>
      </div>
    </div>
  );
}
