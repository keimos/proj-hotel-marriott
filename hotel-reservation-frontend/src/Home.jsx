import { Link } from "react-router-dom";

function Home() {
    return (
        <div className="container">
            <h1>Welcome to Hotel Registration</h1>
            <Link to="/reserve">
                <button>Book a Reservation</button>
            </Link>
        </div>
    );
}

export default Home;