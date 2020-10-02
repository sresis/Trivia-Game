const Router = ReactRouterDOM.BrowserRouter;
const Route = ReactRouterDOM.Route;
const Link = ReactRouterDOM.Link;
const Prompt = ReactRouterDOM.Prompt;
const Switch = ReactRouterDOM.Switch;
const Redirect = ReactRouterDOM.Redirect;
const Autocomplete = React;
const {Button, Alert, Col, Row, Card, CardColumns, CardGroup, Container, Collapse, 
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

function ChooseCategory() {

    return(
        <Container fluid="md" id="choose-category">
            <h1>Choose a category!</h1>
        </Container>
    )
}

ReactDOM.render(<App />, document.getElementById('root'))