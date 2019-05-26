import { Link } from 'gatsby';
import PropTypes from 'prop-types';
import React from 'react';
import Icon from '../images/verdun-icon.svg';

const Header = ({ siteTitle }) => (
  <header
    style={{
      background: `rebeccapurple`,
      marginBottom: `1.45rem`,
      padding: `1.45rem 1.0875rem`,
      display: 'flex'
    }}
  >
    <Link
      to="/"
      style={{
        width: '6rem',
        marginRight: '1rem'
      }}
    >
      <Icon />
    </Link>
  </header>
);

Header.propTypes = {
  siteTitle: PropTypes.string
};

Header.defaultProps = {
  siteTitle: ``
};

export default Header;
