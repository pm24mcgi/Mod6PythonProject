import Demo from "../auth/Demo";

const SplashPage = () => {
	return (
		<div className="splashPageBody">
			<div className="splash-header">
				<img src='/images/logo-white.svg' alt="logo"></img>
				<h2 className='splashSubtitle'>Book unique places to stay and things to do. Vacation Rentals, Homes, Experiences and Places.</h2>
				<p>Try us by clicking below:</p>
				<Demo />
			</div>
		</div>
	);
};

export default SplashPage;
