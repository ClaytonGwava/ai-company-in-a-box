import { useState } from "react";
import axios from "axios";
import ReactMarkdown from "react-markdown";
import remarkGfm from "remark-gfm";

function App() {
  const [idea, setIdea] = useState("");
  const [result, setResult] = useState<Record<string, string> | null>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);
    setError(null);
    setResult(null);

    try {
      const response = await axios.post("http://localhost:8000/run", { idea });
      let output = response.data.output;

      // Ensure output is a parsed object
      if (typeof output === "string") {
        try {
          output = JSON.parse(output);
        } catch {
          // leave as string if parse fails
          output = { Result: output };
        }
      }

      // Filter out any empty or undefined segments
      const cleanedOutput: Record<string, string> = {};
      for (const [key, value] of Object.entries(output)) {
        if (value) cleanedOutput[key] = value as string;
      }

      setResult(cleanedOutput);
    } catch (err: any) {
      setError(err.response?.data?.detail || err.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen w-full bg-gradient-to-br from-gray-50 to-gray-200 flex items-center justify-center px-4 py-10">
      <div className="w-full max-w-6xl bg-white shadow-2xl rounded-xl p-6 sm:p-8 md:p-10">
        <h1 className="text-2xl sm:text-3xl md:text-4xl font-bold text-gray-800 mb-6 text-center">
          🚀 Multi-Agent Company In A Box
        </h1>

        {/* Input form */}
        <form onSubmit={handleSubmit} className="space-y-4 mb-6">
          <input
            type="text"
            value={idea}
            onChange={(e) => setIdea(e.target.value)}
            placeholder="Enter your project idea..."
            className="w-full px-4 py-3 text-base border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 text-black"
          />

          <button
            type="submit"
            className="w-full bg-blue-600 hover:bg-blue-700 text-white text-base font-semibold py-3 rounded-lg transition duration-200 disabled:opacity-60"
            disabled={loading}
          >
            {loading ? "Running..." : "Run Workflow"}
          </button>
        </form>

        {/* Feedback states */}
        {loading && (
          <p className="mt-4 text-blue-500 font-medium animate-pulse text-center">
            ⏳ Processing...
          </p>
        )}
        {error && (
          <p className="mt-4 text-red-600 font-semibold text-center">{error}</p>
        )}

        {/* Output */}
        {result && Object.keys(result).length > 0 && (
          <div className="mt-6 grid grid-cols-1 md:grid-cols-2 gap-6 max-h-[70vh] overflow-auto">
            {Object.entries(result).map(([role, content]) => (
              <div
                key={role}
                className="bg-gray-50 border border-gray-300 rounded-lg p-6 shadow-sm"
              >
                <h2 className="text-lg font-bold text-blue-700 mb-4">
                  {role.toUpperCase()}
                </h2>
                <div className="prose prose-blue max-w-none text-gray-800">
                  <ReactMarkdown remarkPlugins={[remarkGfm]}>
                    {content.replace(/\\n/g, "\n")}
                  </ReactMarkdown>
                </div>
              </div>
            ))}
          </div>
        )}
      </div>
    </div>
  );
}

export default App;
