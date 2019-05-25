var proxy = require('http-proxy-middleware');

module.exports = {
  siteMetadata: {
    title: `Verdun`,
    description: `Cluster`,
    author: `@gatsbyjs`
  },
  plugins: [
    `gatsby-plugin-react-helmet`,
    {
      resolve: `gatsby-source-filesystem`,
      options: {
        name: `images`,
        path: `${__dirname}/src/images`
      }
    },
    `gatsby-transformer-sharp`,
    `gatsby-plugin-sharp`,
    {
      resolve: `gatsby-plugin-manifest`,
      options: {
        name: `gatsby-starter-default`,
        short_name: `starter`,
        start_url: `/`,
        background_color: `#663399`,
        theme_color: `#663399`,
        display: `minimal-ui`,
        icon: `src/images/verdun-icon.svg` // This path is relative to the root of the site.
      }
    },
    // this (optional) plugin enables Progressive Web App + Offline functionality
    // To learn more, visit: https://gatsby.dev/offline
    // `gatsby-plugin-offline`,
    {
      resolve: `gatsby-plugin-lodash`,
      options: {
        disabledFeatures: [
          'shorthands',
          'cloning',
          'currying',
          'caching',
          'collections',
          'exotics',
          'guards',
          'metadata',
          'deburring',
          'unicode',
          'chaining',
          'memoizing',
          'coercions',
          'flattening',
          'paths',
          'placeholders'
        ]
      }
    },
    {
      resolve: 'gatsby-plugin-react-svg',
      options: {
        rule: {
          include: /images/
        }
      }
    },
    {
      resolve: `gatsby-plugin-material-ui`,
      // If you want to use styled components, in conjunction to Material-UI, you should:
      // - Change the injection order
      // - Add the plugin
      options: {
        // stylesProvider: {
        //   injectFirst: true,
        // },
      }
      // 'gatsby-plugin-styled-components',
    }
  ],
  developMiddleware: app => {
    app.use(
      '/metrics',
      proxy({
        target: 'https://verdun.patrician.gold',
        changeOrigin: true
      })
    );
  }
};
