import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Home from "./Home";
import Reserve from "./Reserve";
import Success from "./Success";
import ErrorPage from "./ErrorPage";

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/reserve" element={<Reserve />} />
        <Route path="/success" element={<Success />} />
        <Route path="*" element={<ErrorPage />} />
      </Routes>
    </Router>
  );
}

export default App;