#configure server with Puppet
class { 'nginx':
  package_ensure => 'present',
  service_ensure => 'running',
  service_enable => true,
}
file { 'etc/nginx/sites-available/default':
  ensure => 'file',
  content => template('nginx/default.erb'),
  notify => service['nginx'],
}
file { 'var/www/html/index.html':
  ensure  => 'file',
  content => 'Hello World!',
}
file { '/var/www/html/404.html':
  ensure  => 'file',
  content => "Ceci n'est pas une page",
}
service { 'nginx':
  ensure     => 'running',
  enable     => true,
  require    => File['/etc/nginx/sites-available/default'],
}
nginx::resource::vhost { 'default':
  ensure    => present,
  www_root  => '/var/www/html',
  listen_port => 80,
  location_cfg_append => {
    '/' => {
      'try_files' => '$uri $uri/ =404',
    },
    '/redirect_me' => {
      'return' => '301 https://www.example.com',
    },
    '~* \.html$' => {
      'error_page' => '404 /404.html',
    },
  },
}
