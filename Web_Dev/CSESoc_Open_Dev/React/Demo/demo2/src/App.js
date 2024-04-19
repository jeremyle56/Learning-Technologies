import { useEffect, useState } from "react";
import "./App.css";
import Button from "./components/Button";

function App() {
  const [data, setData] = useState(null);
  const [isLoading, setIsLoading] = useState(true);
  const [isError, setIsError] = useState(false);
  useEffect(() => {
    const fetchData = async () => {
      let data;
      try {
        const resp = await fetch("https://randomuser.me/api");
        if (!resp.ok) throw new Error("oh no");
        data = await resp.json();
      } catch {
        setIsError(true);
        return;
      }
      setData(data);
      setIsLoading(false);
    };

    fetchData();
  }, []);

  if (isLoading) return <p> Loading...</p>
  if (isError) return <p> oh no</p>
  
  return (
    <div className="App">
      <br />
      <br />
      <Button bg="blue" msg="Click me!" onClick={() => {
        alert('Yay!');
      }}> Click me! </Button>
      <Button bg="red" msg="Don't click me!" onClick={() => {
        alert('NOOOO!');
      }}> Don't click me! </Button>

      <pre>{JSON.stringify(data)}</pre>
    </div>
  );
}

export default App;

/* Fetching Using Changing Data
const Component = ({ x }) => {
  const [data , setData] = useState("");
  const [loading, setLoading] = useState(true);
  useEffect(() => {
    const controller = new AbortController();
    
    const fetchData = async () => {
      setLoading(true);
      const resp = await fetch(`${API_ROOT}/${x}`, {
        signal: controller.signal
      });
      const data = await resp.json();
      setData(data);
      setLoading(false);
    };

    fetchData();

    return () => {
      controller.abort();
    }
  }, [x]);

  if (loading) {
    return <LoadingSpinner />;
  }

  return <div>Data: {data}</div>;
}
*/