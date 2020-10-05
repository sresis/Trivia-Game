const Router = ReactRouterDOM.BrowserRouter;
const Route = ReactRouterDOM.Route;
const Link = ReactRouterDOM.Link;
const Prompt = ReactRouterDOM.Prompt;
const Switch = ReactRouterDOM.Switch;
const Redirect = ReactRouterDOM.Redirect;
const Autocomplete = React;
const {Button, Alert, Dropdown, ButtonGroup, DropdownButton, Col, Row, Card, CardColumns, CardGroup, Container, Collapse, 
    Form, FormControl, Nav, Navbar, Radio, Spinner, Popover, InputGroup } = ReactBootstrap;
    

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
                    <Route path='/category-questions/:api_id' component={CategoryQuestion}>
                        <CategoryQuestion />
                    </Route>
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
                    <Dropdown.Item
                    key = {data[idx]['api_id']}
                    onClick={()=> history.push(`/category-questions/${data[idx]['api_id']}`)} >
                        {data[idx]['category_name']}
                    </Dropdown.Item>
                );
            }
            setCategory(cat_info);
        })
        // reset to avoid infinite loop
    }, [props.category_name, props.api_id])

    return(
        <Container fluid="md" id="choose-category">
            <h1>Choose a category!</h1>
            
            <DropdownButton id="dropdown-cat" title="Choose a Category!">
                {category}
            </DropdownButton>
        </Container>
    )
}

function CategoryQuestion(props) {
    // pulls the API category ID from the route
    const {api_id} = ReactRouterDOM.useParams();

    const question_data = {'question': props.question}

    // stores question details to be shown in HTML
    const[question, setQuestion] = React.useState([]);
    const history = ReactRouterDOM.useHistory();
    const [incorrectAnswer, setIncorrectAnswer] = React.useState([]);
    const possible_answers = []

    React.useEffect(() => {

        
        fetch(`/api/category/${api_id}`, {
            method: 'POST',
			credentials: 'include',
			headers: {
				'Content-Type': 'application/json'
			},
        })
        .then(res => res.json())
        .then(data => {
            
            // add correct answer to possible answers
            const correct_ans = data.correct_answer;
            console.log(correct_ans);
            possible_answers.push(
                <ul>{correct_ans}</ul>
            )
            const question_info = data.question;
            const incorrect = data.incorrect_answers;
            for(const item of incorrect) {
                possible_answers.push(
                <ul>{item}</ul>
                )
            }
            
            setQuestion(question_info);
            setIncorrectAnswer(possible_answers);
        })
        
    }, [props.question])

    // get the question info
    return (
        <Form.Group>
            <Form.Label>{question}</Form.Label>
                <div>
                    {incorrectAnswer}
                </div>
         
        </Form.Group>
    )

}

ReactDOM.render(<App />, document.getElementById('root'))