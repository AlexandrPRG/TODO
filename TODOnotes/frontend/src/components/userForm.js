import React from "react";

class UserForm extends React.Component {
  constructor(props) {
    super(props)
    this.state = {username: '', email: ''}
  }
  handleChange(event) {
    this.setState({
        [event.target.name]: event.target.value
    })
  }
  handleSubmit(event) {
    this.props.create_user(this.state.login, this.state.password)
    event.preventDefault()
  }
  handleUserChange(event) {

  }
    render() {
    return (
      <form onSubmit={(event) => this.handleSubmit(event)}>
        <input
          type="text"
          name="login"
          placeholder="login"
          value={this.state.login}
          onChange={(event) => this.handleChange(event)}
        />
        <input
          type="password"
          name="password"
          placeholder="password"
          value={this.state.password}
          onChange={(event) => this.handleChange(event)}
        />
        <input
          type="submit"
          value="Login"
        />
      </form>
      )
  }
}
export default UserForm