const Router = ReactRouterDOM.BrowserRouter;
const Route = ReactRouterDOM.Route;
const Link = ReactRouterDOM.Link;
const Prompt = ReactRouterDOM.Prompt;
const Switch = ReactRouterDOM.Switch;
const Redirect = ReactRouterDOM.Redirect;
const Autocomplete = React;
const {Button, Alert, Dropdown, Col, Row, Card, CardColumns, CardGroup, Container, Collapse, 
    Form, FormControl, Nav, Navbar, Spinner, Popover } = ReactBootstrap;
    

// instance of context
const LoginContext = React.createContext(null);

// handle showing component
function App () {

    return (
        <Router>
            <div>
                <nav className="navbar navbar-expand-lg navbar-light bg-light">
                <ul className="navbar-nav mr-auto">
                    <Link to={'/'} className="nav-link"> Home </Link>
                    <Link to={'/choose-category'} className="nav-link">Choose Category</Link>
                </ul>
                </nav>
                <hr />
                <Switch>
                    <Route exact path='/' component={Homepage} />
                    <Route path='/choose-category' component={ChooseCategory} />
                </Switch>
            </div>
      </Router>
    );
}

function Homepage() {

    return(
        <Container fluid="md" id="homepage">
            <h1>Welcome to the trivia game!</h1>
        </Container>
    )
}

function ChooseCategory(props) {
    // store the category details to be displayed
    const category_details = {'category_name': props.category_name, 'api_id': props.api_id}
    
    const [category, setCategory] = React.useState([]);
    const history = ReactRouterDOM.useHistory();

    // get the category data from the server
    React.useEffect(() => {

        fetch('/api/categories', {

            headers: {
                'Content-Type': 'application/json'
            },
        })
        .then(response => response.json())
        .then(data => {
            const cat_info = []
            // loop and get all user info
            for (const idx in data) {
                cat_info.push(
                    <div>
                        {data[idx]['category_name']}
                    </div>
                );
            }
            setCategory(cat_info);
        })
        // reset to avoid infinite loop
    }, [props.category_name, props.api_uri])


    return(
        <Container fluid="md" id="choose-category">
            <h1>Choose a category!</h1>
            <div>
                {category}
            </div>
            <Dropdown
                title = "Select Category"
                list = {category}
            />
        </Container>
    )
}

ReactDOM.render(<App />, document.getElementById('root'))