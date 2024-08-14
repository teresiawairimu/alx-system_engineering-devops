# Fixes a typo in wp-settings.php
file { '/var/www/html/wp-settings.php':
  ensure => file,
  owner => 'www-data',
  group => 'www-data',
  mode => '0644',
}
exec { 'fix-wordpress-typo':
  command => "/bin/sed -i 's/class-wp-locale.phpp/class-wp-locale.php/' /var/www/html/wp-settings.php",
  onlyif  => "/bin/grep -q 'class-wp-locale.phpp' /var/www/html/wp-settings.php",
  require => File['/var/www/html/wp-settings.php'],
}
service { 'apache2':
  ensure => running,
  require => Exec['fix-wordpress-typo'],
}

