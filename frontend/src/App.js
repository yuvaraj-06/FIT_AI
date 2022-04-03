import React, { Component } from "react";

import ExerciseCard from "./components/ExerciseCard";
import "./style.scss";
import "bootstrap/dist/css/bootstrap.min.css";

import pushup from "./assets/pushup.png";
import skipping from "./assets/skipping.png";
import lunges from "./assets/lunges.png";
import pullup from "./assets/pullup.png";
import weight from "./assets/weight.png";
import situps from "./assets/situps.png";
import earth from "./assets/earth.png";

import { Button, Modal, ModalHeader, ModalBody, ModalFooter } from "reactstrap";

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      modal: false,
    };

    this.toggle = this.toggle.bind(this);
  }

  toggle() {
    this.setState({
      modal: !this.state.modal,
    });
  }

  render() {
    return (
      <main>
        <Modal isOpen={this.state.modal} size="lg" toggle={this.toggle} className="primary-modal" centered>
          <ModalHeader toggle={this.toggle}>Pushups</ModalHeader>
          <ModalBody>
            <img src={earth} alt="" />
          </ModalBody>
        </Modal>

        <div className="card-container">
          <ExerciseCard img={pushup} title="Pushups" onClick={this.toggle} />
          <ExerciseCard img={skipping} title="Skipping" onClick={this.toggle} />
          <ExerciseCard img={lunges} title="Lunges" onClick={this.toggle} />
          <ExerciseCard img={pullup} title="Pullup" onClick={this.toggle} />
          <ExerciseCard img={weight} title="Weight Lifting" onClick={this.toggle} />
          <ExerciseCard img={situps} title="Situps" onClick={this.toggle} />
        </div>
      </main>
    );
  }
}

export default App;
