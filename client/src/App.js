import { Route, Switch } from 'react-router-dom';

import Main from './views/Main';

function App() {
  return (
    <div className="App">
      <Switch>
        <Route exact path="/">
          <Main />
        </Route>
      </Switch>
    </div>
  );
}

export default App;
