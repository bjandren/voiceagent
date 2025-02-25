import { useState } from "react";
import { Button } from "./components/ui/button";
import "./App.css";

function App() {
  const [count, setCount] = useState(0);

  return (
    <div className="flex min-h-screen flex-col items-center justify-center bg-secondary-lightGray p-4">
      <div className="w-full max-w-md rounded-lg bg-neutral-white p-8 shadow-md">
        <h1 className="mb-6 text-center text-2xl font-bold text-primary-darkBlue">
          AI-Driven Customer Support Agent
        </h1>

        <div className="space-y-4">
          <p className="text-center text-secondary-gray">
            Denna demo visar UI-komponenter för vår SaaS-baserade
            AI-kundsupportagent för fastighetsbolag.
          </p>

          <div className="flex justify-center gap-2">
            <Button
              variant="default"
              onClick={() => setCount((count) => count + 1)}
            >
              Räkna: {count}
            </Button>

            <Button variant="destructive">Radera</Button>
          </div>

          <div className="flex justify-center gap-2">
            <Button variant="outline">Kontur</Button>
            <Button variant="secondary">Sekundär</Button>
          </div>

          <div className="flex justify-center gap-2">
            <Button variant="ghost">Ghost</Button>
            <Button variant="link">Länk</Button>
            <Button variant="success">Framgång</Button>
          </div>
        </div>

        <p className="mt-6 text-center text-sm text-secondary-gray">
          Implementerar färgpalett från <code>color-palette.md</code>
        </p>
      </div>
    </div>
  );
}

export default App;
