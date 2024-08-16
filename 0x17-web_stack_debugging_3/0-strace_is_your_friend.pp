# Fixes a typo in wp-settings.php
exec { 'fix-wordpress-typo':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/usr/local/bin/:/bin/'
}

