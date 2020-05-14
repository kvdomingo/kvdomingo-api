import React, { Component, lazy } from 'react';
import {
    MDBContainer as Container,
    MDBIcon as Icon,
} from 'mdbreact';
import { Link, Switch, Route, withRouter } from 'react-router-dom';
import { BaseContext } from '../App';
import Loading from '../Loading';
import TitleComponent from '../TitleComponent';
import './Svip.css';

const Gallery = lazy(() => import('./Gallery'));
const Post = lazy(() => import('./Post'));


export default withRouter(class Subject extends Component {
    static contextType = BaseContext;

    constructor(props) {
        super(props);
        this.state = {
            activePage: '',
            courses: [],
            coursesIsLoaded: false,
            posts: [],
            subject: '',
        };

        this.handleActivePill = this.handleActivePill.bind(this);
        this.togglePills = this.togglePills.bind(this);
    }

    componentDidMount() {
        this.handleActivePill();
        let { courseSlug } = this.props.match.params;
        fetch(`/api/svip/blogpost?subject__slug=${courseSlug}`)
            .then(res => res.json())
            .then(posts => this.setState({ posts }));
        fetch('/api/svip/course')
            .then(res => res.json())
            .then(courses => {
                let subject = courses.find(course => (course.slug === courseSlug));
                this.setState({
                    courses,
                    coursesIsLoaded: true,
                    subject,
                });
            });
    }

    componentDidUpdate(prevProps, prevState) {
        if (this.state.activePage !== prevState.activePage) {
            this.handleActivePill();
        }
    }

    handleActivePill() {
        let url = window.location.pathname;
        let activePage = url.split('/').slice(-1)[0];
        this.setState({ activePage });
    }

    togglePills(e, activePage) {
        this.setState({ activePage });
    }

    render() {
        let { path } = this.props.match;
        let { courseSlug } = this.props.match.params;
        return (
            <React.Fragment>
                <TitleComponent title={`${this.state.subject.name} | Coursework`} />
                {(!this.state.coursesIsLoaded)
                    ? <Loading />
                    : <Container className='my-5'>

                        <Route path={`${path}/:postSlug`}>
                            <div className='mb-3'>
                                <Link to={`/${this.context}/svip/${courseSlug}`}>
                                    <Icon fas icon='angle-left' className='mr-1' /> Back to {this.state.subject.name}
                                </Link>
                            </div>
                            <Post posts={this.state.posts} subject={this.state.subject} />
                        </Route>

                        <Route exact path={path}>
                            <div className='mb-3'>
                                <Link to={`/${this.context}/svip`}>
                                    <Icon fas icon='angle-left' className='mr-1' /> Back to courses
                                </Link>
                            </div>
                            <Gallery key={this.state.activePage} { ...this.state } />
                        </Route>

                    </Container>}
            </React.Fragment>
        );
    }
})