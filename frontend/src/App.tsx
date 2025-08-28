import { useState } from "react";
import axios from "axios";

function App() {
  const [idea, setIdea] = useState("");
  const [result, setResult] = useState<string | null>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);
    setError(null);
    setResult(null);

    try {
      const response = await axios.post("http://localhost:8000/run", { idea });
      setResult(JSON.stringify(response.data.output, null, 2));
    } catch (err: any) {
      setError(err.response?.data?.detail || err.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen w-full bg-gradient-to-br from-gray-50 to-gray-200 flex items-center justify-center px-4 py-10">
      <div className="w-full max-w-md sm:max-w-xl md:max-w-2xl bg-white shadow-2xl rounded-xl p-6 sm:p-8 md:p-10">
        <h1 className="text-2xl sm:text-3xl md:text-4xl font-bold text-gray-800 mb-6 text-center">
          🚀 Multi-Agent Company In A Box
        </h1>

        <form onSubmit={handleSubmit} className="space-y-4">
          <input
            type="text"
            value={idea}
            onChange={(e) => setIdea(e.target.value)}
            placeholder="Enter your project idea..."
            className="w-full px-4 py-3 text-base border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
          />

          <button
            type="submit"
            className="w-full bg-blue-600 hover:bg-blue-700 text-white text-base font-semibold py-3 rounded-lg transition duration-200 disabled:opacity-60"
            disabled={loading}
          >
            {loading ? "Running..." : "Run Workflow"}
          </button>
        </form>

        {loading && (
          <p className="mt-4 text-blue-500 font-medium animate-pulse text-center">
            ⏳ Processing...
          </p>
        )}

        {error && (
          <p className="mt-4 text-red-600 font-semibold text-center">{error}</p>
        )}

        {result && (
          <div className="mt-6 bg-gray-100 border border-gray-300 rounded-lg p-4 overflow-auto max-h-[60vh]">
            <h2 className="text-lg font-semibold text-gray-700 mb-2">🧠 Output:</h2>
            <pre className="text-sm sm:text-base text-gray-800 whitespace-pre-wrap break-words">
              {result}
            </pre>
          </div>
        )}
      </div>
    </div>
  );
}

export default App;
