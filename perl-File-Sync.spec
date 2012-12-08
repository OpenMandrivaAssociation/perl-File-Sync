%define upstream_name    File-Sync
%define upstream_version 0.09

Name:      perl-%{upstream_name}
Version:   %perl_convert_version %{upstream_version}
Release:   10

Summary:   Perl access to fsync() and sync() function calls
License:   Artistic
Group:     Development/Perl
Url:       http://search.cpan.org/dist/%{upstream_name}
Source0:   http://search.cpan.org//CPAN/authors/id/C/CE/CEVANS/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl-devel


%description
The fsync() function takes a Perl file handle as its only argument, and
passes its fileno() to the C function fsync().  It returns I<undef> on
failure, or I<true> on success.

The fsync_fd() function is used internally by fsync(); it takes a file
descriptor as its only argument.

The sync() function is identical to the C function sync().

This module does B<not> export any methods by default, but fsync() is
made available as a method of the I<FileHandle> and I<IO::Handle>
classes.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make CFLAGS="%{optflags}"

%check
%__make test

%install
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%{perl_vendorarch}/File
%{perl_vendorarch}/auto/File
%{_mandir}/man3/*


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 0.90.0-9mdv2012.0
+ Revision: 765257
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 0.90.0-8
+ Revision: 763765
- rebuilt for perl-5.14.x
- cleanup temporary deps, this was added in perl-devel instead

* Fri Jan 20 2012 Oden Eriksson <oeriksson@mandriva.com> 0.90.0-7
+ Revision: 763245
- force it
- rebuild

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 0.90.0-6
+ Revision: 667145
- mass rebuild

* Sun Apr 03 2011 Funda Wang <fwang@mandriva.org> 0.90.0-5
+ Revision: 650045
- rebuild

* Sun Aug 01 2010 Funda Wang <fwang@mandriva.org> 0.90.0-4mdv2011.0
+ Revision: 564436
- rebuild for perl 5.12.1

* Tue Jul 20 2010 Sandro Cazzaniga <kharec@mandriva.org> 0.90.0-3mdv2011.0
+ Revision: 555283
- rebuild

  + JÃ©rÃ´me Quelin <jquelin@mandriva.org>
    - rebuild for 5.12

* Tue Jul 28 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.90.0-1mdv2010.1
+ Revision: 401660
- rebuild using %%perl_convert_version
- fixed license field

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 0.09-8mdv2009.0
+ Revision: 257016
- rebuild

* Mon Jan 14 2008 Pixel <pixel@mandriva.com> 0.09-6mdv2008.1
+ Revision: 151424
- rebuild for perl-5.10.0

* Wed Dec 26 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.09-5mdv2008.1
+ Revision: 137999
- spec cleanup

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Fri Sep 30 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.09-4mdk
- Buildrequires fix

* Thu Sep 29 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.09-3mdk
- Fix url

* Fri Jul 08 2005 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.09-2mdk
- drop arch restriction

* Sun Mar 27 2005 Bruno Cornec <bcornec@mandrake.org> 0.09-1mdk
- Initial build.

