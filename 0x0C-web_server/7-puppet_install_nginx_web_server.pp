# install and configure nginx server
# site.pp

# Install Nginx package
package { 'nginx':
  ensure => installed,
}

# Ensure Nginx service is running and enabled
service { 'nginx':
  ensure  => running,
  enable  => true,
  require => Package['nginx'],
}

# Define Nginx configuration file
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => template('nginx/default.erb'),
  require => Package['nginx'],
  notify  => Service['nginx'],
}

# Manage default site symlink to sites-enabled
file { '/etc/nginx/sites-enabled/default':
  ensure => 'link',
  target => '/etc/nginx/sites-available/default',
  notify => Service['nginx'],
}

# Nginx should listen on port 80
nginx::resource::server { 'default':
  listen_port => '80',
}

# Custom template for Nginx default configuration
# This template includes both serving 'Hello World!' on root and handling redirect
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => template('nginx/default.erb'),
  require => Package['nginx'],
  notify  => Service['nginx'],
}

# Notify Nginx service to reload after template changes
service { 'nginx':
  ensure  => running,
  require => File['/etc/nginx/sites-available/default'],
  notify  => Service['nginx'],
}
