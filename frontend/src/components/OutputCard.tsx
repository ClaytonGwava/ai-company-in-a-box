interface OutputCardProps {
  role: string;
  content: string;
}

export default function OutputCard({ role, content }: OutputCardProps) {
  return (
    <div className="bg-white shadow rounded-xl p-6 border border-gray-200 mb-6">
      <h2 className="text-xl font-bold mb-4 text-blue-700">{role}</h2>
      <div
        className="prose max-w-none whitespace-pre-line"
        dangerouslySetInnerHTML={{ __html: content.replace(/\n/g, "<br/>") }}
      />
    </div>
  );
}
